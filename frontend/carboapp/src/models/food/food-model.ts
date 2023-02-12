import type { MeasureEnum } from "../enums/measure-enum";
import { MeasureTypeEnum } from "../enums/measure-type-enum";

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
        public quantity: number = 0,
        public quantityType: MeasureTypeEnum = MeasureTypeEnum.KG,
        public isFavorite: boolean = false,
        public user: FoodUserInfo = new FoodUserInfo(),
        public description?: string,
        public measure?: MeasureEnum,
        public measureQuantity?: number,
    ){

    }
}