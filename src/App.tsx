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

 const handleRemovePreference = () => {
    setPreferences((prevPreferences) => {
      const newPreferences = [...prevPreferences];
      newPreferences.pop();
      return newPreferences;
    });
 };

  return (
    <div className="">
      <div className='container bg-secondary'>
        <div className='row'>
          <div className="col bg-info text-center">
            <AddButton buttonClicked={handleAddPreference}/>
          </div>
          <div className="col bg-warning text-center">
            <SubtractButton buttonClicked={handleRemovePreference}/>
          </div>
        </div>
      </div>
      <PrefContainer preferences={preferences}/>
    </div>
  );
}

export default App
