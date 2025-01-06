import React from 'react';

interface props {
    buttonClicked: () => void;
}

const addButton = ({buttonClicked}: props) => {
    return (
        <>
            <button type="button" className="btn btn-outline-success" id="addButton"
            onClick={buttonClicked}>&#43;</button>
        </>
    );
};

export default addButton;
