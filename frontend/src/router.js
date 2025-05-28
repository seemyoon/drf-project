import {createBrowserRouter, Navigate} from "react-router-dom";
import MainLayout from "./layout/MainLayout";
import {LoginPage} from "./page/LoginPage";
import PizzasPage from "./page/PizzasPage";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {
                index: true, element: <Navigate to={'login'}/>
            },
            {
                path: 'login', element: <LoginPage/>
            },
            {
                path: 'pizzas', element: <PizzasPage/>
            }
        ]
    }
])

export {router}