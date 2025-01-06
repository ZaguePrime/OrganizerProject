import PrefInput from './preferencesInput';

interface PreferencesContainerProps {
  preferences: { id: number }[]; // Define the props with an array of preference objects
}

const PreferencesContainer = ({ preferences }: PreferencesContainerProps) => {
  return (
    <div className="preferences-container">
      {preferences.map((pref) => (
        <PrefInput key={pref.id} />
      ))}
    </div>
  );
};

export default PreferencesContainer;
