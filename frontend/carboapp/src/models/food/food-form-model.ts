import type { MeasureEnum } from "../enums/measure-enum"
import { MeasureTypeEnum } from "../enums/measure-type-enum";

export default class FoodFormModel{
    constructor(
        public carbo: number = 0,
        public name: string = '',
        public quantity: number = 0,
        public quantityType: MeasureTypeEnum = MeasureTypeEnum.MG,
        public userId: number = 0,
        public description?: string,
        public measure?: MeasureEnum,
        public measureQuantity?: number
    ){}
}