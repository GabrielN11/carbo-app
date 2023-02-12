import type { MeasureEnum } from "../enums/measure-enum";

export class FoodUserInfo{
    constructor(
        public id: number = 0,
        public name: string = ''
    ){}
}

export default class FoodModel{
    constructor(
        public id: number = 0,
        public name: string = '',
        public carbo: number = 0,
        public isFavorite: boolean = false,
        public user: FoodUserInfo = new FoodUserInfo,
        public description?: string,
        public quantity?: number,
        public measure?: MeasureEnum,
        public measureQuantity?: number,
    ){

    }
}