import { apiDelete } from "$lib/api/api";
import type { SuccessfullyMessageResponse } from "$lib/api/api-models";
import type FoodFormModel from "../../../../models/food/food-form-model";

export default async function deleteFood(id: number): Promise<SuccessfullyMessageResponse> {
    const res = await apiDelete<SuccessfullyMessageResponse>(`/food/${id}`, true)

    return res
}