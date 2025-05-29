import {authService} from "./authService";
import {w3cwebsocket} from "websocket";

const baseURL = 'ws://localhost/api'

const socketService = async () => {
    const {data: {token}} = await authService.getSocketToken();

    return {
        chat: (room) => new w3cwebsocket(`${baseURL}/chat/${room}/?token=${token}`),
        pizzas: () => new w3cwebsocket(`${baseURL}/pizzas/?token=${token}`)
    }
}

export {
    socketService
}