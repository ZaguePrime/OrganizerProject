import '../preferencesInput.css';
// interface PreferencesInputProps {

// }

const preferencesInput = () => {

    return (
        <div className = "container text-center">
            <div className = "row gx-0">
                <div className = "col">
                    <label className="form-label">Folder Name</label>
                    <input type="text" className="form-control foldername-input"></input>
                </div>
                <div className = "col">
                    <label className="form-label">Regex or Text to match</label>
                    <input type="text" className="form-control regex-text"></input>
                </div>
            </div>
        </div>
    );
};

export default preferencesInput;