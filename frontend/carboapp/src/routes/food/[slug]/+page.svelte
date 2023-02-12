<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import Card, { Content } from "@smui/card";
	import List, { Item, Text } from "@smui/list";
    import getFoodById from "$lib/api/endpoints/food/get-food-by-id";
    import { isEmpty, toNumber } from "lodash-es";
    import { onMount, afterUpdate } from "svelte";
    import FoodModel from "../../../models/food/food-model";
    import { displayToast } from "../../../stores/toast-store";
    import Tooltip, { Wrapper } from '@smui/tooltip';
    import { MeasureTypeMock } from "$lib/mocks/measure-type-mock";
    import { MeasureEnum } from "../../../models/enums/measure-enum";
    import { user } from "../../../stores/user-store";
    import Menu from "@smui/menu";
    import DeleteFood from "../../../components/delete-food/delete-food.svelte";
    import AddFood from "../../../components/add-food/add-food.svelte";
    import deleteFavorite from "$lib/api/endpoints/favorite/delete-favorite";
    import postFavorite from "$lib/api/endpoints/favorite/post-favorite";
    import FavoriteModel from "../../../models/favorite/favorite-model";

    let id: number;
    let menu: Menu;

    let food: FoodModel = new FoodModel();
    let favorite: boolean = false;

    let openDelete: boolean = false;
    let openEdit: boolean = false;

    async function fetchFood() {
        try {
            const res = await getFoodById(id);

            food = res.data;
            favorite = res.data.isFavorite;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
            goto('/')
        }
    }

    async function handleFavorite(){
        try{
            const res = favorite ? await deleteFavorite(id) : await postFavorite(new FavoriteModel(id))

            favorite = !favorite
            displayToast(res.message, '#28a745', 1500)
        }catch(e: any){
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
                {#if $user && $user.id === food.user.id}
                    
                        <Wrapper>
                            <button on:click={() => menu.setOpen(true)} class='settings-btn'>
                            <iconify-icon icon="material-symbols:settings" class='favorite-btn' style="color: white;" width=25 ></iconify-icon>
                            </button>
                            <Tooltip>Opções</Tooltip>
                        </Wrapper>
                    <Menu bind:this={menu}>
                        <List>
                          <Item on:SMUI:action={() => (openEdit = true)}>
                            <Text>Editar</Text>
                          </Item>
                          <Item on:SMUI:action={() => (openDelete = true)}>
                            <Text>Excluir</Text>
                          </Item>
                        </List>
                      </Menu>

                      <DeleteFood id={id} open={openDelete} name={food.name} closeDialog={() => (openDelete = false)}/>
                      <AddFood open={openEdit} closeHandler={() => {
                        openEdit = false
                        fetchFood()
                      }} id={food.id}
                        name={food.name} carbo={food.carbo} description={food.description} measure={food.measure}
                        measureQuantity={food.measureQuantity} measureType={food.quantityType} quantity={food.quantity}/>
                {:else}
                    <p>Publicado por {food.user.name}</p>
                {/if}
            </div>
            {#if $user}
            <div class='favorite'>
                {#if favorite}
                    <Wrapper>
                        <button class='settings-btn' on:click={handleFavorite}>
                        <iconify-icon icon="material-symbols:favorite" style="color: #d20d0d;" class='favorite-btn' width=25></iconify-icon>
                        </button>
                        <Tooltip>Remover Favorito</Tooltip>
                     </Wrapper>
                {:else}
                    <Wrapper>
                        <button class='settings-btn' on:click={handleFavorite}>
                        <iconify-icon icon="material-symbols:favorite-outline" class='favorite-btn' style="color: gray;" width=25></iconify-icon>
                        </button>
                        <Tooltip>Favoritar</Tooltip>
                    </Wrapper>
                {/if}
            </div>
            {/if}
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
        width: 256px;
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

    .favorite-btn{
        cursor: pointer;
    }

    .settings-btn{
        background: unset;
        border: none;
    }

    @media(min-width: 600px){
        .card-container{
            width: 400px;
        }
    }

</style>
