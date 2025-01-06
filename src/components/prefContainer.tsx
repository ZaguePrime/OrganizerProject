import PrefInput from './preferencesInput';

interface PreferencesContainerProps {
  preferences: { id: number }[]; // Define the props with an array of preference objects
  buttonClicked: (id?:number) => void;
}

const PreferencesContainer = ({ preferences, buttonClicked }: PreferencesContainerProps) => {
  return (
    <div className="preferences-container text-center">
      {preferences.map((pref) => (
        <PrefInput pref_id={pref.id} buttonClicked={()=>buttonClicked(pref.id)}/>
      ))}
    </div>
  );
};

export default PreferencesContainer;
