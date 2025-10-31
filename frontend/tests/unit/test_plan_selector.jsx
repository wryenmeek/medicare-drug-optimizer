import { render, screen } from '@testing-library/react';
import PlanSelector from '../../src/components/PlanSelector';

describe('PlanSelector component', () => {
  it('should render the title', () => {
    render(<PlanSelector />);
    expect(screen.getByText(/Plan Selection/i)).toBeInTheDocument();
  });
});
