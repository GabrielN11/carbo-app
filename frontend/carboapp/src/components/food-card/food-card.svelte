<script lang='ts'>
    import { goto } from '$app/navigation';
    import {
    Item,
    Meta,
    Text,
    PrimaryText,
    SecondaryText,
  } from '@smui/list';
    import Tooltip, { Wrapper } from '@smui/tooltip';
    import type FoodModel from '../../models/food/food-model';

  export let food: FoodModel;
</script>

<Item
    on:SMUI:action={() => goto(`/food/${food.id}`)}
>
    <Text>
        <PrimaryText>{food.name}</PrimaryText>
        <SecondaryText>{food.description || ''}</SecondaryText>
    </Text>
    <Meta>
        <Wrapper>
            <iconify-icon icon="ph:info-thin" style="color: white;" width=30></iconify-icon>
            <Tooltip>Carboidratos: {food.carbo}g</Tooltip>
        </Wrapper>
    </Meta>
</Item>
