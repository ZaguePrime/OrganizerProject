import '../preferencesInput.css';
// interface PreferencesInputProps {

// }

const preferencesInput = () => {

    return (
        <div className = "container d-inline-flex justify-content-center bg-secondary">
            <div className = "row gx-0">
                <div className = "col">
                    <label className="form-label d-flex justify-content-center">Folder Name</label>
                    <input type="text" className="form-control foldername-input"></input>
                </div>
                <div className = "col">
                    <label className="form-label d-flex justify-content-center">Regex or Text to match</label>
                    <input type="text" className="form-control regex-text"></input>
                </div>
            </div>
        </div>
    );
};

export default preferencesInput;