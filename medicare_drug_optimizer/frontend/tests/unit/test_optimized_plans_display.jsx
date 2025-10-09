// frontend/tests/unit/test_optimized_plans_display.jsx

import { render, screen } from '@testing-library/react';
import OptimizedPlansDisplay from '../../src/components/OptimizedPlansDisplay';

describe('OptimizedPlansDisplay component', () => {
  it('should render the title', () => {
    render(<OptimizedPlansDisplay />);
    expect(screen.getByText(/Optimized Plans Display/i)).toBeInTheDocument();
  });
});
