import '../preferencesInput.css';
// interface PreferencesInputProps {

// }
import SubtractButton from './subtractButton';

const preferencesInput = () => {

    return (
        <div key='' className = "container d-inline-flex justify-content-center bg-secondary">
            <div className = "row gx-5">
                <div className = "col">
                    <label className="form-label d-flex justify-content-center">Folder</label>
                    <input type="text" className="form-control foldername-input"></input>
                </div>
                <div className = "col">
                    <label className="form-label d-flex justify-content-center">Match</label>
                    <input type="text" className="form-control regex-text"></input>
                </div>
                <div className = "col d-flex align-items-center">
                    <SubtractButton buttonClicked={() => {}}/>
                </div>
            </div>
        </div>
    );
};

export default preferencesInput;