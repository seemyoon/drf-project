import {useEffect, useState} from "react";
import {pizzaService} from "../services/pizzaService";
import PizzaComponent from "./PizzaComponent";

const PizzasComponent = () => {
    const [pizzas, setPizzas] = useState([])


    useEffect(() => {
        pizzaService.getAll().then((data) => {
            setPizzas(data.data.data);
        })
        // data, because we set data in pagination
    }, [])
    return (
        <div>
            {pizzas.map(pizza => <PizzaComponent key={pizza.id} pizza={pizza}/>)}
        </div>
    );
};

export default PizzasComponent;