<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import Card, { Content } from "@smui/card";
    import getFoodById from "$lib/api/endpoints/food/get-food-by-id";
    import { isEmpty, toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import FoodModel from "../../../models/food/food-model";
    import { displayToast } from "../../../stores/toast-store";
    import { MeasureMock } from "$lib/mocks/measure-mock";
    import { MeasureTypeMock } from "$lib/mocks/measure-type-mock";
    import { MeasureEnum } from "../../../models/enums/measure-enum";

    let id: number;

    let food: FoodModel = new FoodModel();

    async function fetchFood() {
        try {
            const res = await getFoodById(id);

            food = res.data;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
        }
    }

    onMount(() => {
        try {
            id = toNumber($page.url.pathname.split("/")[2]);

            if (isNaN(id)) throw new Error();

            fetchFood();
        } catch (e: any) {
            goto("/");
        }
    });
</script>

<svelte:head>
    <title>Carbo App - {food.name}</title>
    <meta
        name="description"
        content={food.description || `Carboidratos do alimento ${food.name}`}
    />
</svelte:head>

<section>
    {#if !isEmpty(food.name)}
        <h1>{food.name}</h1>
        {#if !isEmpty(food.description)}
            <p class="description">{food.description}</p>
        {/if}
        <div class="card-container">
            <div>
                <Card variant="outlined">
                    <Content>
                        <div class="card-content">
                            <p>Quantidade</p>
                            <p class="info">
                                {food.quantity}
                                {MeasureTypeMock.find(
                                    (x) => x.key === food.quantityType
                                )?.description}
                            </p>
                        </div>
                    </Content>
                </Card>
            </div>

            <div>
                <Card variant="outlined">
                    <Content>
                        <div class="card-content">
                            <p>Carboidratos</p>
                            <p class="info">{food.carbo}g</p>
                        </div>
                    </Content>
                </Card>
            </div>

            {#if food.measure && food.measureQuantity}
                <div class='measure'>
                    <Card variant="outlined">
                        <Content>
                            <div class="card-content">
                                <p>Medida de Referência</p>
                                {#if food.measure === MeasureEnum.SCOOP}
                                    <iconify-icon icon="mdi:silverware-spoon" style="color: #2e254f;" width='40'></iconify-icon>
                                    <p class='info'>{food.measureQuantity} Colher(es)</p>
                                {:else if food.measure === MeasureEnum.SPOON}
                                    <iconify-icon icon="game-icons:ice-cream-scoop" style="color: #2e254f;" width='40'></iconify-icon>
                                    <p class='info'>{food.measureQuantity} Concha(s)</p>
                                {:else if food.measure === MeasureEnum.CUP}
                                    <iconify-icon icon="mdi:cup-full" style="color: #2e254f;" width='40'></iconify-icon>
                                    <p class='info'>{food.measureQuantity} Copo(s)</p>
                                {:else if food.measure === MeasureEnum.TEACUP}
                                    <iconify-icon icon="bi:cup-hot" style="color: #2e254f;" width='40'></iconify-icon>
                                    <p class='info'>{food.measureQuantity} Xícara(s)</p>
                                {:else}
                                    <iconify-icon icon="mdi:food-apple-outline" style="color: #2e254f;" width='40'></iconify-icon>
                                    <p class='info'>{food.measureQuantity} Unidade(s)</p>
                                {/if}
                            </div>
                        </Content>
                    </Card>
                </div>
            {/if}
            <div>
                <p>Publicado por {food.user.name}</p>
            </div>
            <div class='favorite'>
                {#if food.isFavorite}
                    <iconify-icon icon="material-symbols:favorite" style="color: #d20d0d;" width=25></iconify-icon>
                {:else}
                    <iconify-icon icon="material-symbols:favorite-outline" style="color: gray;" width=25></iconify-icon>
                {/if}
            </div>
        </div>
    {/if}
</section>

<style>
    section {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 30px;
    }

    .description {
        margin-top: 0;
    }

    .card-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .card-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #2e254f;
    }

    .measure{
        grid-column-start: 1;
        grid-column-end: 3;
    }

    .info {
        margin: 0;
        font-size: 1.5rem;
    }

    .favorite{
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
</style>
