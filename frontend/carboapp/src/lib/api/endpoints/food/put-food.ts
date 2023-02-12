import { apiPut } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type FoodFormModel from "../../../../models/food/food-form-model";

interface FoodId{
    id: number;
}

export default async function alterFood(model: FoodFormModel): Promise<SuccessfullyResponse<FoodId>> {
    const res = await apiPut<SuccessfullyResponse<FoodId>, FoodFormModel>('/food', model, true)

    return res
}