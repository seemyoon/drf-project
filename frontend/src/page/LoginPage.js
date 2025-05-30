import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {useNavigate} from "react-router-dom";


const LoginPage = () => {
    const {register, handleSubmit} = useForm();
    const navigate = useNavigate()


    const onSubmit = async (user) => {
        await authService.login(user) // store token in LS
        navigate('/pizzas')
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder={'email'} {...register('email')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <button>login</button>
        </form>
    );
};

export {LoginPage};