// frontend/tests/unit/test_drug_coverage_display.jsx

import { render, screen } from '@testing-library/react';
import DrugCoverageDisplay from '../../src/components/DrugCoverageDisplay';

describe('DrugCoverageDisplay component', () => {
  it('should render the title', () => {
    render(<DrugCoverageDisplay />);
    expect(screen.getByText(/Drug Coverage Display/i)).toBeInTheDocument();
  });
});
