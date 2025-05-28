import PizzasComponent from "../component/PizzasComponent";
import Chat from "../component/Chat";
import PizzaForm from "../component/PizzaForm";

const PizzasPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <Chat/>
        </div>
    );
};

export default PizzasPage;