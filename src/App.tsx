import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PreferencesInput from './components/preferencesInput'
import AddButton from './components/addButton'

function App() {
  return (
    <div className="bg-success">
      <AddButton/>
      <PreferencesInput/>
    </div>
  );
}

export default App
