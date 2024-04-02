import React from 'react'
import ActiveBlock from './active_block.jsx'
import Board from './board.jsx'

function Body () {
    return <div style = {{'width': '100%', 'height': 1000, 'marginTop': 1, 'border': 'solid'}}>
                <h3>Body</h3>
                <ActiveBlock />
                <ActiveBlock />
                <ActiveBlock />
                <ActiveBlock />
                <ActiveBlock />
                <Board />
            </div>
}

export default Body