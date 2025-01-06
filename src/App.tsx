import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PrefContainer from './components/prefContainer'
import PreferencesInput from './components/preferencesInput'
import AddButton from './components/addButton'

interface Preference {
  id: number; // Define the structure of each preference
  folderName: string;
  regexText: string;
}

function App() {

  const [preferences, setPreferences] = useState<Preference[]>([]);

  const handleAddPreference = () => {
    setPreferences((prevPreferences) => [
      ...prevPreferences,
      { id: prevPreferences.length, folderName: '', regexText: '' },
    ]);
  };

  return (
    <div className="bg-success">
      <AddButton buttonClicked={handleAddPreference}/>
      <PrefContainer preferences={preferences}/>
    </div>
  );
}

export default App
