import '../preferencesInput.css';
// interface PreferencesInputProps {

// }
import SubtractButton from './subtractButton';

interface props {
    pref_id: number;
    buttonClicked: (num_id?:number) => void;
}

const preferencesInput = ({pref_id, buttonClicked} : props) => {

    return (
        <div key={pref_id} className = "container d-inline-flex justify-content-center bg-secondary">
            <div className = "row gx-5">
                <div className = "col">
                    <label className="form-label d-flex justify-content-center align-items-center">Folder</label>
                    <input type="text" className="form-control foldername-input"></input>
                </div>
                <div className = "col">
                    <label className="form-label d-flex justify-content-center align-items-center">Match</label>
                    <input type="text" className="form-control regex-text"></input>
                </div>
                <div className = "col d-flex justify-content-center align-items-center">
                    <SubtractButton id={pref_id} buttonClicked={()=>buttonClicked(pref_id)}/>
                </div>
            </div>
        </div>
    );
};

export default preferencesInput;