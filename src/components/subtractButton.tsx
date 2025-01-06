import React from 'react';

interface props {
    id: number
    buttonClicked: (id?:number) => void;
}

const subtractButton = ({id, buttonClicked}: props) => {
    return (
        <>
            <button type="button" className="btn btn-outline-info" id="subtractButton"
            onClick={()=>buttonClicked(id)}>&#x2212;</button>
        </>
    );
};

export default subtractButton;