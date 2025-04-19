import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [pizzas, setPizzas] = useState([])

    useEffect(() => {
        axios
            .get('/api/pizzas')
            .then(({data})=>{setPizzas(data.data)})
    }, [])

    console.log(pizzas)
    return (
        <div>
            {pizzas.map(pizza =>
                <div key={pizza.id}>
                    <h2>Pizza's name: {pizza.name}</h2>
                    <h2>Pizza's size: {pizza.size}</h2>
                    <h2>Pizza's price: {pizza.price}</h2>
                    <h2>Pizza's size: {pizza.size}</h2>
                </div>)}
        </div>
    );
};

export default App;