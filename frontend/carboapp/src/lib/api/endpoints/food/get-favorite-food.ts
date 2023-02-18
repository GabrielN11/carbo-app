import { apiGet } from "$lib/api/api";
import type { SuccessfullyListResponse } from "$lib/api/api-models";
import type FoodModel from "../../../../models/food/food-model";

export default async function getFavoriteFood(id: number, page: number): Promise<SuccessfullyListResponse<FoodModel>>{
    const offsetPage = `?page=${page}`

    const food = await apiGet<SuccessfullyListResponse<FoodModel>>(`/favorite/${id}${offsetPage}`, false)
    return food
}