# Aggregates all Language/Version and Primary Dependencies from every plan.md in /specs
function Aggregate-PlanData {
    $specsDir = Join-Path $REPO_ROOT 'medicare_drug_optimizer/specs'
    $langSet = @{}
    $frameworkSet = @{}
    $planFiles = Get-ChildItem -Path $specsDir -Recurse -Filter 'plan.md' | Select-Object -ExpandProperty FullName
    foreach ($planFile in $planFiles) {
        $langRaw = Extract-PlanField -FieldPattern 'Language/Version' -PlanFile $planFile
        $frameworkRaw = Extract-PlanField -FieldPattern 'Primary Dependencies' -PlanFile $planFile
        if ($langRaw) {
            foreach ($lang in ($langRaw -split ',')) {
                $langSet[$lang.Trim()] = $true
            }
        }
        if ($frameworkRaw) {
            foreach ($fw in ($frameworkRaw -split ',')) {
                $frameworkSet[$fw.Trim()] = $true
            }
        }
    }
    $script:NEW_LANG = ($langSet.Keys | Where-Object { $_ -and $_ -ne 'N/A' -and $_ -ne 'NEEDS CLARIFICATION' } | Sort-Object | ForEach-Object { "- $_" }) -join "`n"
    $script:NEW_FRAMEWORK = ($frameworkSet.Keys | Where-Object { $_ -and $_ -ne 'N/A' -and $_ -ne 'NEEDS CLARIFICATION' } | Sort-Object | ForEach-Object { "- $_" }) -join "`n"
    return $true
}
#!/usr/bin/env pwsh
<#!
.SYNOPSIS
Update agent context files with information from plan.md (PowerShell version)

.DESCRIPTION
Mirrors the behavior of scripts/bash/update-agent-context.sh:
 1. Environment Validation
 2. Plan Data Extraction
 3. Agent File Management (create from template or update existing)
 4. Content Generation (technology stack, recent changes, timestamp)
 5. Multi-Agent Support (claude, gemini, copilot, cursor, qwen, opencode, codex, windsurf, kilocode, auggie, roo, q)

.PARAMETER AgentType
Optional agent key to update a single agent. If omitted, updates all existing agent files (creating a default Claude file if none exist).

.EXAMPLE
./update-agent-context.ps1 -AgentType claude

.EXAMPLE
./update-agent-context.ps1   # Updates all existing agent files

.NOTES
Relies on common helper functions in common.ps1
#>
param(
    [Parameter(Position = 0)]
    [ValidateSet('claude', 'gemini', 'copilot', 'cursor', 'qwen', 'opencode', 'codex', 'windsurf', 'kilocode', 'auggie', 'roo', 'q')]
    [string]$AgentType
)

$ErrorActionPreference = 'Stop'

# Import common helpers
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. (Join-Path $ScriptDir 'common.ps1')

# Acquire environment paths
$envData = Get-FeaturePathsEnv
$REPO_ROOT = $envData.REPO_ROOT
$CURRENT_BRANCH = $envData.CURRENT_BRANCH
$HAS_GIT = $envData.HAS_GIT
$IMPL_PLAN = $envData.IMPL_PLAN
$NEW_PLAN = $IMPL_PLAN

# Agent file paths
$CLAUDE_FILE = Join-Path $REPO_ROOT 'CLAUDE.md'
$GEMINI_FILE = Join-Path $REPO_ROOT 'medicare_drug_optimizer/GEMINI.md'
$COPILOT_FILE = Join-Path $REPO_ROOT '.github/copilot-instructions.md'
$CURSOR_FILE = Join-Path $REPO_ROOT '.cursor/rules/specify-rules.mdc'
$QWEN_FILE = Join-Path $REPO_ROOT 'QWEN.md'
$AGENTS_FILE = Join-Path $REPO_ROOT 'AGENTS.md'
$WINDSURF_FILE = Join-Path $REPO_ROOT '.windsurf/rules/specify-rules.md'
$KILOCODE_FILE = Join-Path $REPO_ROOT '.kilocode/rules/specify-rules.md'
$AUGGIE_FILE = Join-Path $REPO_ROOT '.augment/rules/specify-rules.md'
$ROO_FILE = Join-Path $REPO_ROOT '.roo/rules/specify-rules.md'
$Q_FILE = Join-Path $REPO_ROOT 'AGENTS.md'

$TEMPLATE_FILE = Join-Path $REPO_ROOT '.specify/templates/agent-file-template.md'

# Parsed plan data placeholders
$script:NEW_LANG = ''
$script:NEW_FRAMEWORK = ''
$script:NEW_DB = ''
$script:NEW_PROJECT_TYPE = ''

function Write-Info { 
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    Write-Host "INFO: $Message" 
}

function Write-Success { 
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    Write-Host "$([char]0x2713) $Message" 
}

function Write-WarningMsg { 
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    Write-Warning $Message 
}

function Write-Err { 
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    Write-Host "ERROR: $Message" -ForegroundColor Red 
}

function Validate-Environment {
    if (-not $CURRENT_BRANCH) {
        Write-Err 'Unable to determine current feature'
        if ($HAS_GIT) { Write-Info "Make sure you're on a feature branch" } else { Write-Info 'Set SPECIFY_FEATURE environment variable or create a feature first' }
        exit 1
    }
    if (-not (Test-Path $NEW_PLAN)) {
        Write-Err "No plan.md found at $NEW_PLAN"
        Write-Info 'Ensure you are working on a feature with a corresponding spec directory'
        if (-not $HAS_GIT) { Write-Info 'Use: $env:SPECIFY_FEATURE=your-feature-name or create a new feature first' }
        exit 1
    }
    if (-not (Test-Path $TEMPLATE_FILE)) {
        Write-Err "Template file not found at $TEMPLATE_FILE"
        Write-Info 'Run specify init to scaffold .specify/templates, or add agent-file-template.md there.'
        exit 1
    }
}

function Extract-PlanField {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FieldPattern,
        [Parameter(Mandatory = $true)]
        [string]$PlanFile
    )
    if (-not (Test-Path $PlanFile)) { return '' }
    $regex = '^\*\*\s*' + [Regex]::Escape($FieldPattern) + '\s*\*\*\s*:\s*(.*)$'
    Write-Host "DEBUG: Extracting field '$FieldPattern' with regex: $regex"
    $lines = Get-Content -LiteralPath $PlanFile -Encoding utf8
    foreach ($line in $lines) {
        Write-Host "DEBUG: Line: $line"
        $match = [regex]::Match($line, $regex, 'IgnoreCase')
        if ($match.Success -and $match.Groups.Count -ge 2) {
            $val = $match.Groups[1].Value.Trim()
            Write-Host "DEBUG: Matched value: $val"
            if ($val -notin @('NEEDS CLARIFICATION', 'N/A')) {
                return $val
            }
        }
    }
    return ''
    $regex = "^\*\*\s*$FieldPattern\s*\*\*\s*:\s*(.*)$"
    $lines = Get-Content -LiteralPath $PlanFile -Encoding utf8
    foreach ($line in $lines) {
        $match = [regex]::Match($line, $regex, 'IgnoreCase')
        if ($match.Success -and $match.Groups.Count -ge 3) {
            $val = $match.Groups[2].Value.Trim()
            if ($val -notin @('NEEDS CLARIFICATION', 'N/A')) {
                return $val
            }
        }
    }
    return ''
}

function Parse-PlanData {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PlanFile
    )
    if (-not (Test-Path $PlanFile)) { Write-Err "Plan file not found: $PlanFile"; return $false }
    Write-Info "Parsing plan data from $PlanFile"
    $langRaw = Extract-PlanField -FieldPattern 'Language/Version' -PlanFile $PlanFile
    $frameworkRaw = Extract-PlanField -FieldPattern 'Primary Dependencies' -PlanFile $PlanFile
    # Format as bulleted lists if comma-separated
    if ($langRaw) {
        $langList = ($langRaw -split ',') | ForEach-Object { '- ' + $_.Trim() }
        $script:NEW_LANG = ($langList -join [Environment]::NewLine).Trim()
    }
    else { $script:NEW_LANG = '' }
    if ($frameworkRaw) {
        $frameworkList = ($frameworkRaw -split ',') | ForEach-Object { '- ' + $_.Trim() }
        $script:NEW_FRAMEWORK = ($frameworkList -join [Environment]::NewLine).Trim()
    }
    else { $script:NEW_FRAMEWORK = '' }
    $script:NEW_DB = Extract-PlanField -FieldPattern 'Storage' -PlanFile $PlanFile
    $script:NEW_PROJECT_TYPE = Extract-PlanField -FieldPattern 'Project Type' -PlanFile $PlanFile

    if ($NEW_LANG) { Write-Info "Found language: $NEW_LANG" } else { Write-WarningMsg 'No language information found in plan' }
    if ($NEW_FRAMEWORK) { Write-Info "Found framework: $NEW_FRAMEWORK" }
    if ($NEW_DB -and $NEW_DB -ne 'N/A') { Write-Info "Found database: $NEW_DB" }
    if ($NEW_PROJECT_TYPE) { Write-Info "Found project type: $NEW_PROJECT_TYPE" }
    return $true
}

function Format-TechnologyStack {
    param(
        [Parameter(Mandatory = $false)]
        [string]$Lang,
        [Parameter(Mandatory = $false)]
        [string]$Framework
    )
    $parts = @()
    if ($Lang -and $Lang -ne 'NEEDS CLARIFICATION') { $parts += $Lang }
    if ($Framework -and $Framework -notin @('NEEDS CLARIFICATION', 'N/A')) { $parts += $Framework }
    if (-not $parts) { return '' }
    return ($parts -join ' + ')
}

function Get-ProjectStructure { 
    param(
        [Parameter(Mandatory = $false)]
        [string]$ProjectType
    )
    if ($ProjectType -match 'web') { return "backend/`nfrontend/`ntests/" } else { return "src/`ntests/" } 
}

function Get-CommandsForLanguage { 
    param(
        [Parameter(Mandatory = $false)]
        [string]$Lang
    )
    switch -Regex ($Lang) {
        'Python' { return 'cd src; pytest; ruff check .' }
        'Rust' { return 'cargo test; cargo clippy' }
        'JavaScript|TypeScript' { return 'npm test; npm run lint' }
        default { return "# Add commands for $Lang" }
    }
}

function Get-LanguageConventions { 
    param(
        [Parameter(Mandatory = $false)]
        [string]$Lang
    )
    if ($Lang) { "${Lang}: Follow standard conventions" } else { 'General: Follow standard conventions' } 
}

function New-AgentFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetFile,
        [Parameter(Mandatory = $true)]
        [string]$ProjectName,
        [Parameter(Mandatory = $true)]
        [datetime]$Date
    )
    if (-not (Test-Path $TEMPLATE_FILE)) { Write-Err "Template not found at $TEMPLATE_FILE"; return $false }
    $temp = New-TemporaryFile
    Copy-Item -LiteralPath $TEMPLATE_FILE -Destination $temp -Force

    $projectStructure = Get-ProjectStructure -ProjectType $NEW_PROJECT_TYPE
    $commands = Get-CommandsForLanguage -Lang $NEW_LANG
    $languageConventions = Get-LanguageConventions -Lang $NEW_LANG

    $escaped_lang = $NEW_LANG
    $escaped_framework = $NEW_FRAMEWORK
    $escaped_branch = $CURRENT_BRANCH

    $content = Get-Content -LiteralPath $temp -Raw -Encoding utf8
    $content = $content -replace '\[PROJECT_NAME\]', $ProjectName
    $content = $content -replace '\[DATE\]', $Date.ToString('yyyy-MM-dd')
    
    # Build the technology stack string safely
    $techStackForTemplate = ''
    if ($escaped_lang -and $escaped_framework) {
        $techStackForTemplate = "- $escaped_lang + $escaped_framework ($escaped_branch)"
    }
    elseif ($escaped_lang) {
        $techStackForTemplate = "- $escaped_lang ($escaped_branch)"
    }
    elseif ($escaped_framework) {
        $techStackForTemplate = "- $escaped_framework ($escaped_branch)"
    }
    
    $content = $content -replace '\[EXTRACTED FROM ALL PLAN.MD FILES\]', $techStackForTemplate
    # For project structure we manually embed (keep newlines)
    $escapedStructure = [Regex]::Escape($projectStructure)
    $content = $content -replace '\[ACTUAL STRUCTURE FROM PLANS\]', $escapedStructure
    # Replace escaped newlines placeholder after all replacements
    $content = $content -replace '\[ONLY COMMANDS FOR ACTIVE TECHNOLOGIES\]', $commands
    $content = $content -replace '\[LANGUAGE-SPECIFIC, ONLY FOR LANGUAGES IN USE\]', $languageConventions
    
    # Build the recent changes string safely
    $recentChangesForTemplate = ''
    if ($escaped_lang -and $escaped_framework) {
        $recentChangesForTemplate = "- ${escaped_branch}: Added ${escaped_lang} + ${escaped_framework}"
    }
    elseif ($escaped_lang) {
        $recentChangesForTemplate = "- ${escaped_branch}: Added ${escaped_lang}"
    }
    elseif ($escaped_framework) {
        $recentChangesForTemplate = "- ${escaped_branch}: Added ${escaped_framework}"
    }
    
    $content = $content -replace '\[RECENT_CHANGES\]', $recentChangesForTemplate
    # Convert literal \n sequences introduced by Escape to real newlines
    $content = $content -replace '\\n', [Environment]::NewLine

    $parent = Split-Path -Parent $TargetFile
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent | Out-Null }
    Set-Content -LiteralPath $TargetFile -Value $content -NoNewline -Encoding utf8
    Remove-Item $temp -Force
    return $true
}

function Update-ExistingAgentFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetFile,
        [Parameter(Mandatory = $true)]
        [datetime]$Date
    )
    if (-not (Test-Path $TargetFile)) { return (New-AgentFile -TargetFile $TargetFile -ProjectName (Split-Path $REPO_ROOT -Leaf) -Date $Date) }

    $techStack = Format-TechnologyStack -Lang $NEW_LANG -Framework $NEW_FRAMEWORK
    $newTechEntries = @()
    if ($techStack) {
        $escapedTechStack = [Regex]::Escape($techStack)
        if (-not (Select-String -Pattern $escapedTechStack -Path $TargetFile -Quiet)) { 
            $newTechEntries += "- $techStack ($CURRENT_BRANCH)" 
        }
    }
    if ($NEW_DB -and $NEW_DB -notin @('N/A', 'NEEDS CLARIFICATION')) {
        $escapedDB = [Regex]::Escape($NEW_DB)
        if (-not (Select-String -Pattern $escapedDB -Path $TargetFile -Quiet)) { 
            $newTechEntries += "- $NEW_DB ($CURRENT_BRANCH)" 
        }
    }
    $newChangeEntry = ''
    if ($techStack) { $newChangeEntry = "- ${CURRENT_BRANCH}: Added ${techStack}" }
    elseif ($NEW_DB -and $NEW_DB -notin @('N/A', 'NEEDS CLARIFICATION')) { $newChangeEntry = "- ${CURRENT_BRANCH}: Added ${NEW_DB}" }

    $content = Get-Content -LiteralPath $TargetFile -Raw -Encoding utf8
    $content = $content -replace '\[PROJECT_NAME\]', (Split-Path $REPO_ROOT -Leaf)
    # Replace the Core Technologies section
    $langBlock = $script:NEW_LANG.Trim()
    if ($langBlock) {
        $content = $content -replace '(?ms)(## Core Technologies\s*-)(.*?)(\n##|\n$)', "`$1`n$langBlock`n`$3"
    }
    else {
        $content = $content -replace '(?ms)(## Core Technologies\s*-)(.*?)(\n##|\n$)', "`$1`n`$3"
    }
    $frameworkBlock = $script:NEW_FRAMEWORK.Trim()
    if ($frameworkBlock) {
        $content = $content -replace '(?ms)(## Key Libraries\s*-)(.*?)(\n##|\n$)', "`$1`n$frameworkBlock`n`$3"
    }
    else {
        $content = $content -replace '(?ms)(## Key Libraries\s*-)(.*?)(\n##|\n$)', "`$1`n`$3"
    }
    # Build the recent changes string safely
    $recentChangesForTemplate = ''
    if ($NEW_LANG -and $NEW_FRAMEWORK) {
        $recentChangesForTemplate = "- ${CURRENT_BRANCH}: Added ${NEW_LANG} + ${NEW_FRAMEWORK}"
    }
    elseif ($NEW_LANG) {
        $recentChangesForTemplate = "- ${CURRENT_BRANCH}: Added ${NEW_LANG}"
    }
    elseif ($NEW_FRAMEWORK) {
        $recentChangesForTemplate = "- ${CURRENT_BRANCH}: Added ${NEW_FRAMEWORK}"
    }
    $content = $content -replace '\[RECENT_CHANGES\]', $recentChangesForTemplate
    Set-Content -LiteralPath $TargetFile -Value $content -Encoding utf8
    return $true
}

function Update-AgentFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetFile,
        [Parameter(Mandatory = $true)]
        [string]$AgentName
    )
    if (-not $TargetFile -or -not $AgentName) { Write-Err 'Update-AgentFile requires TargetFile and AgentName'; return $false }
    Write-Info "Updating $AgentName context file: $TargetFile"
    $projectName = Split-Path $REPO_ROOT -Leaf
    $date = Get-Date

    $dir = Split-Path -Parent $TargetFile
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

    if (-not (Test-Path $TargetFile)) {
        if (New-AgentFile -TargetFile $TargetFile -ProjectName $projectName -Date $date) { Write-Success "Created new $AgentName context file" } else { Write-Err 'Failed to create new agent file'; return $false }
    }
    else {
        try {
            if (Update-ExistingAgentFile -TargetFile $TargetFile -Date $date) { Write-Success "Updated existing $AgentName context file" } else { Write-Err 'Failed to update agent file'; return $false }
        }
        catch {
            Write-Err "Cannot access or update existing file: $TargetFile. $_"
            return $false
        }
    }
    return $true
}

function Update-SpecificAgent {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Type
    )
    switch ($Type) {
        'claude' { Update-AgentFile -TargetFile $CLAUDE_FILE -AgentName 'Claude Code' }
        'gemini' { Update-AgentFile -TargetFile $GEMINI_FILE -AgentName 'Gemini CLI' }
        'copilot' { Update-AgentFile -TargetFile $COPILOT_FILE -AgentName 'GitHub Copilot' }
        'cursor' { Update-AgentFile -TargetFile $CURSOR_FILE -AgentName 'Cursor IDE' }
        'qwen' { Update-AgentFile -TargetFile $QWEN_FILE -AgentName 'Qwen Code' }
        'opencode' { Update-AgentFile -TargetFile $AGENTS_FILE -AgentName 'opencode' }
        'codex' { Update-AgentFile -TargetFile $AGENTS_FILE -AgentName 'Codex CLI' }
        'windsurf' { Update-AgentFile -TargetFile $WINDSURF_FILE -AgentName 'Windsurf' }
        'kilocode' { Update-AgentFile -TargetFile $KILOCODE_FILE -AgentName 'Kilo Code' }
        'auggie' { Update-AgentFile -TargetFile $AUGGIE_FILE -AgentName 'Auggie CLI' }
        'roo' { Update-AgentFile -TargetFile $ROO_FILE -AgentName 'Roo Code' }
        'q' { Update-AgentFile -TargetFile $Q_FILE -AgentName 'Amazon Q Developer CLI' }
        default { Write-Err "Unknown agent type '$Type'"; Write-Err 'Expected: claude|gemini|copilot|cursor|qwen|opencode|codex|windsurf|kilocode|auggie|roo|q'; return $false }
    }
}

function Update-AllExistingAgents {
    $found = $false
    $ok = $true
    if (Test-Path $CLAUDE_FILE) { if (-not (Update-AgentFile -TargetFile $CLAUDE_FILE -AgentName 'Claude Code')) { $ok = $false }; $found = $true }
    if (Test-Path $GEMINI_FILE) { if (-not (Update-AgentFile -TargetFile $GEMINI_FILE -AgentName 'Gemini CLI')) { $ok = $false }; $found = $true }
    if (Test-Path $COPILOT_FILE) { if (-not (Update-AgentFile -TargetFile $COPILOT_FILE -AgentName 'GitHub Copilot')) { $ok = $false }; $found = $true }
    if (Test-Path $CURSOR_FILE) { if (-not (Update-AgentFile -TargetFile $CURSOR_FILE -AgentName 'Cursor IDE')) { $ok = $false }; $found = $true }
    if (Test-Path $QWEN_FILE) { if (-not (Update-AgentFile -TargetFile $QWEN_FILE -AgentName 'Qwen Code')) { $ok = $false }; $found = $true }
    if (Test-Path $AGENTS_FILE) { if (-not (Update-AgentFile -TargetFile $AGENTS_FILE -AgentName 'Codex/opencode')) { $ok = $false }; $found = $true }
    if (Test-Path $WINDSURF_FILE) { if (-not (Update-AgentFile -TargetFile $WINDSURF_FILE -AgentName 'Windsurf')) { $ok = $false }; $found = $true }
    if (Test-Path $KILOCODE_FILE) { if (-not (Update-AgentFile -TargetFile $KILOCODE_FILE -AgentName 'Kilo Code')) { $ok = $false }; $found = $true }
    if (Test-Path $AUGGIE_FILE) { if (-not (Update-AgentFile -TargetFile $AUGGIE_FILE -AgentName 'Auggie CLI')) { $ok = $false }; $found = $true }
    if (Test-Path $ROO_FILE) { if (-not (Update-AgentFile -TargetFile $ROO_FILE -AgentName 'Roo Code')) { $ok = $false }; $found = $true }
    if (Test-Path $Q_FILE) { if (-not (Update-AgentFile -TargetFile $Q_FILE -AgentName 'Amazon Q Developer CLI')) { $ok = $false }; $found = $true }
    if (-not $found) {
        Write-Info 'No existing agent files found, creating default Claude file...'
        if (-not (Update-AgentFile -TargetFile $CLAUDE_FILE -AgentName 'Claude Code')) { $ok = $false }
    }
    return $ok
}

function Print-Summary {
    Write-Host ''
    Write-Info 'Summary of changes:'
    if ($NEW_LANG) { Write-Host "  - Added language: $NEW_LANG" }
    if ($NEW_FRAMEWORK) { Write-Host "  - Added framework: $NEW_FRAMEWORK" }
    if ($NEW_DB -and $NEW_DB -ne 'N/A') { Write-Host "  - Added database: $NEW_DB" }
    Write-Host ''
    Write-Info 'Usage: ./update-agent-context.ps1 [-AgentType claude|gemini|copilot|cursor|qwen|opencode|codex|windsurf|kilocode|auggie|roo|q]'
}

function Main {
    # Robustly resolve plan.md location
    $envData = Get-FeaturePathsEnv
    $REPO_ROOT = $envData.REPO_ROOT
    $CURRENT_BRANCH = $envData.CURRENT_BRANCH
    $IMPL_PLAN = $envData.IMPL_PLAN


    $planPath = $IMPL_PLAN
    if (-not (Test-Path $planPath)) {
        # Fallback: try main feature, else first available feature
        $specsDir = Join-Path $REPO_ROOT 'medicare_drug_optimizer/specs'
        $mainFeatureDir = Join-Path $specsDir 'main'
        $mainPlan = Join-Path $mainFeatureDir 'plan.md'
        if (Test-Path $mainPlan) {
            Write-WarningMsg "No plan.md found for feature $CURRENT_BRANCH, using main plan.md instead."
            $planPath = $mainPlan
        }
        else {
            # Find first available feature directory with plan.md
            $featureDirs = Get-ChildItem -Path $specsDir -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'plan.md') }
            if ($featureDirs.Count -gt 0) {
                $firstPlan = Join-Path $featureDirs[0].FullName 'plan.md'
                Write-WarningMsg "No plan.md found for feature $CURRENT_BRANCH or main; using $firstPlan instead."
                $planPath = $firstPlan
            }
            else {
                Write-Err "No plan.md found for feature $CURRENT_BRANCH, main, or any feature directory."
                Write-Info 'Ensure you are working on a feature with a corresponding spec directory.'
                exit 1
            }
        }
    }

    # Validate template file
    $TEMPLATE_FILE = Join-Path $REPO_ROOT 'medicare_drug_optimizer/.specify/templates/agent-file-template.md'
    if (-not (Test-Path $TEMPLATE_FILE)) {
        Write-Err "Template file not found at $TEMPLATE_FILE"
        Write-Info 'Run specify init to scaffold .specify/templates, or add agent-file-template.md there.'
        exit 1
    }

    Write-Info '=== Aggregating agent context from all plan.md files ==='
    if (-not (Aggregate-PlanData)) { Write-Err 'Failed to aggregate plan data'; exit 1 }
    $success = $true
    if ($AgentType) {
        Write-Info "Updating specific agent: $AgentType"
        if (-not (Update-SpecificAgent -Type $AgentType)) { $success = $false }
    }
    else {
        Write-Info 'No agent specified, updating all existing agent files...'
        if (-not (Update-AllExistingAgents)) { $success = $false }
    }
    Print-Summary
    if ($success) { Write-Success 'Agent context update completed successfully'; exit 0 } else { Write-Err 'Agent context update completed with errors'; exit 1 }
}

Main
