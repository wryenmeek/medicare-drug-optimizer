import { Routes, Route, Link } from 'react-router-dom'
import { Alert } from '@cmsgov/ds-medicare-gov'
import { Button } from '@cmsgov/design-system'
// import CustomComponent from './components/Custom/CustomComponent' // Example for custom component
import DrugAlternativesDisplay from './components/DrugAlternativesDisplay'
import DrugCoverageDisplay from './components/DrugCoverageDisplay'
import PharmacyPreferences from './components/PharmacyPreferences'
import PharmacyRecommendations from './components/PharmacyRecommendations'
import OptimizedPlansDisplay from './components/OptimizedPlansDisplay' // New import
import PlanComparisonDisplay from './components/PlanComparisonDisplay' // New import
import './App.css'

function Home() {
  return (
    <div>
      <h2>Home</h2>
      <p>Welcome to the Medicare Drug Optimizer!</p>
      <Alert heading="Information" type="info">
        This is an example alert from the Medicare.gov Design System.
      </Alert>
      <Button variation="primary">CMS Button</Button>
      {/* <CustomComponent /> */}
    </div>
  )
}

function About() {
  return (
    <div>
      <h2>About</h2>
      <p>This application helps you optimize your Medicare Part D drug costs.</p>
    </div>
  )
}

function App() {
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/alternatives">Drug Alternatives</Link>
          </li>
          <li>
            <Link to="/coverage">Drug Coverage</Link>
          </li>
          <li>
            <Link to="/pharmacy-preferences">Pharmacy Preferences</Link>
          </li>
          <li>
            <Link to="/pharmacy-recommendations">Pharmacy Recommendations</Link>
          </li>
          <li>
            <Link to="/optimized-plans">Optimized Plans</Link> {/* New Link */}
          </li>
          <li>
            <Link to="/plan-comparison">Plan Comparison</Link> {/* New Link */}
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/alternatives" element={<DrugAlternativesDisplay />} />
        <Route path="/coverage" element={<DrugCoverageDisplay />} />
        <Route path="/pharmacy-preferences" element={<PharmacyPreferences />} />
        <Route path="/pharmacy-recommendations" element={<PharmacyRecommendations />} />
        <Route path="/optimized-plans" element={<OptimizedPlansDisplay />} /> {/* New Route */}
        <Route path="/plan-comparison" element={<PlanComparisonDisplay />} /> {/* New Route */}
      </Routes>
    </>
  )
}

export default App