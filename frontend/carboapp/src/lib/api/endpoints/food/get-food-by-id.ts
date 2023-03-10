import { apiGet } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type FoodModel from "../../../../models/food/food-model";

export default async function getFoodById(id: number): Promise<SuccessfullyResponse<FoodModel>>{
    const food = await apiGet<SuccessfullyResponse<FoodModel>>(`/food-by-id/${id}`, true)
    return food
}