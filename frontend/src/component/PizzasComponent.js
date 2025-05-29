import {useEffect, useState} from "react";
import {pizzaService} from "../services/pizzaService";
import PizzaComponent from "./PizzaComponent";
import {socketService} from "../services/socketService";

const PizzasComponent = () => {
    const [pizzas, setPizzas] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        pizzaService.getAll().then((data) => {
            setPizzas(data.data.data);
        })
        // data, because we set data in pagination
    }, [trigger]) // if we have trigger, it will be request for all our API

    useEffect(() => {
        socketInit().then()
    }, [])

    const socketInit = async () => {
        const {pizzas} = await socketService()
        const client = await pizzas()


        client.onopen = () => {
            console.log('pizza socket connected')
            client.send(JSON.stringify({
                action: 'subscribe_to_pizza_model_changes', // subscribe_to_pizza_model_changes the same in file consumer
                request_id: new Date().getTime()
            })) // subscribe for pizzas
        }

        client.onmessage = ({data}) => {
            setTrigger(prev => !prev)
        }
        // This is triggered when a WebSocket message arrives (e.g. someone updated a pizza in the database). Then:
        // 1. trigger changes (true → false → true etc.)
        // 2. This calls useEffect, which depends on trigger
        // 3. A new request is made to pizzaService.getAll()
        // 4. pizzas are updated in useState and page will be reloaded
    }

    return (
        <div>
            {pizzas.map(pizza => <PizzaComponent key={pizza.id} pizza={pizza}/>)}
        </div>
    );
};

export default PizzasComponent;