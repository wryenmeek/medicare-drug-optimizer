// frontend/tests/unit/test_plan_comparison_display.jsx

import { render, screen } from '@testing-library/react';
import PlanComparisonDisplay from '../../src/components/PlanComparisonDisplay';

describe('PlanComparisonDisplay component', () => {
  it('should render the title', () => {
    render(<PlanComparisonDisplay />);
    expect(screen.getByText(/Plan Comparison Display/i)).toBeInTheDocument();
  });
});
