// frontend/tests/unit/test_components.jsx

import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from '../../src/App';

describe('App component', () => {
  it('should render the Home page by default', () => {
    render(
      <MemoryRouter>
        <App />
      </MemoryRouter>
    );
    expect(screen.getByText(/Welcome to the Medicare Drug Optimizer!/i)).toBeInTheDocument();
  });
});
