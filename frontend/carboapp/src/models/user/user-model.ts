export default class UserModel{
    constructor(
        public id: number = 0,
        public username: string = '',
        public email: string = '',
        public password?: string,
        public admin: boolean = false,
        public active: boolean = true,
    ){

    }
}