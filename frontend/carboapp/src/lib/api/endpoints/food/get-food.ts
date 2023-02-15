import { apiGet } from "$lib/api/api";
import type { SuccessfullyListResponse } from "$lib/api/api-models";
import { isEmpty } from "lodash-es";
import type FoodModel from "../../../../models/food/food-model";

export default async function getFood(query: string, page: number): Promise<SuccessfullyListResponse<FoodModel>>{
    const offsetPage = `?page=${page}`
    const queryParam = !isEmpty(query) ? `&search=${query}` : ''

    const food = await apiGet<SuccessfullyListResponse<FoodModel>>(`/food-list${offsetPage}${queryParam}`, false)
    return food
}