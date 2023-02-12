import { apiPost } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";
import type UserLoginModel from "../../../../models/user/user-login-model";
import type UserCreateModel from "../../../../models/user/user-create-model";
import type FoodFormModel from "../../../../models/food/food-form-model";

interface FoodId{
    id: number;
}

export default async function createFood(model: FoodFormModel): Promise<SuccessfullyResponse<FoodId>> {
    const res = await apiPost<SuccessfullyResponse<FoodId>, FoodFormModel>('/food', model, true)

    return res
}