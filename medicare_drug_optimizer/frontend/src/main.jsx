import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { HashRouter } from 'react-router-dom' // Changed from BrowserRouter

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <HashRouter> {/* Changed from BrowserRouter */}
      <App />
    </HashRouter>
  </StrictMode>,
)
