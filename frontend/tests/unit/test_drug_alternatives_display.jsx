// frontend/tests/unit/test_drug_alternatives_display.jsx

import { render, screen } from '@testing-library/react';
import DrugAlternativesDisplay from '../../src/components/DrugAlternativesDisplay';

describe('DrugAlternativesDisplay component', () => {
  it('should render the title', () => {
    render(<DrugAlternativesDisplay />);
    expect(screen.getByText(/Drug Alternatives Display/i)).toBeInTheDocument();
  });
});
