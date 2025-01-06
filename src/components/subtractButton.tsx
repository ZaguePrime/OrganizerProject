import React from 'react';

interface props {
    buttonClicked: () => void;
}

const subtractButton = ({buttonClicked}: props) => {
    return (
        <>
            <button type="button" className="btn btn-outline-info" id="subtractButton"
            onClick={buttonClicked}>&#x2212;</button>
        </>
    );
};

export default subtractButton;