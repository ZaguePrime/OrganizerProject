import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PrefContainer from './components/prefContainer'
import PreferencesInput from './components/preferencesInput'
import AddButton from './components/addButton'
import SubtractButton from './components/subtractButton'

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

  const handleRemovePreference = (id?: number) => {
    setPreferences((prevPreferences) =>
      prevPreferences.filter((pref) => pref.id !== id)
    );
  }

  return (
    <div className="">
      <div className='container bg-secondary'>
        <div className='row'>
          <div className="col bg-info text-center">
            <AddButton buttonClicked={handleAddPreference}/>
          </div>
        </div>
      </div>
      <PrefContainer preferences={preferences} buttonClicked={handleRemovePreference}/>
    </div>
  );
}

export default App
