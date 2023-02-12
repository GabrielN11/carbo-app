<script lang='ts'>
    import Dialog, { Header, Title, Content, Actions } from '@smui/dialog';
    import Select, { Option } from '@smui/select';
    import Button, { Label } from '@smui/button';
    import Textfield from "@smui/textfield";
    import { MeasureEnum } from '../../models/enums/measure-enum';
    import { isEmpty } from 'lodash-es';
    import { MeasureTypeEnum } from '../../models/enums/measure-type-enum';
    import { MeasureTypeMock } from '$lib/mocks/measure-type-mock';
    import { MeasureMock } from '$lib/mocks/measure-mock';
    import { displayToast } from '../../stores/toast-store';
    import FoodFormModel from '../../models/food/food-form-model';
    import { user } from '../../stores/user-store';
    import createFood from '$lib/api/endpoints/food/food-post';

    export let open = true;
    export let closeHandler: () => void;

    //campos
    export let name: string = ''
    export let carbo: number = 0
    export let quantity: number = 0
    export let measureType: MeasureTypeEnum = MeasureTypeEnum.MG
    export let description: string = ''
    export let measure: MeasureEnum = MeasureEnum.UNITY
    export let measureQuantity: number = 0

    let error: boolean[] = [false, false, false]

    function validateField(index: number) {
        if(index === 0){
            if(isEmpty(name)){
                error[0] = true
            }else{
                error[0] = false
            }
        }else if(index === 1){
            if(isEmpty(carbo) || isNaN(Number(carbo))){
                error[1] = true
            }else{
                error[1] = false
            }
        }else{
            if(isEmpty(quantity) || isNaN(Number(quantity))){
                error[2] = true
            }else{
                error[2] = false
            }
        }
    }

    async function handleSubmit(){
        validateField(0)
        validateField(1)
        validateField(2)

        if(error.includes(true)){
            return
        }

        try{
            const res = await createFood(new FoodFormModel(Number(carbo), name, Number(quantity), measureType, $user?.id, description, measure, measureQuantity))

            displayToast(res.message, '#28a745', 4000)
            
            name = ''
            carbo = 0
            quantity = 0
            description = ''
            measureQuantity = 0

            closeHandler()

        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
        }
    }

</script>

<Dialog
  bind:open
  aria-labelledby="fullscreen-title"
  aria-describedby="fullscreen-content"
  on:SMUIDialog:closed={closeHandler}
>
  <Header>
    <Title id="fullscreen-title">Adicionar Alimento</Title>
  </Header>
  <Content id="fullscreen-content">
    <form>
        <fieldset class="fullwidth">
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Nome"
                invalid={error[0]}
                bind:value={name}
                color="secondary"
                on:change={() => validateField(0)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Quantidade"
                invalid={error[2]}
                bind:value={quantity}
                color="secondary"
                on:change={() => validateField(2)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Select variant="filled" bind:value={measureType} label="Tipo de Medida" style='width: 100%'>
                {#each MeasureTypeMock as mt}
                  <Option value={mt.key}>{mt.description}</Option>
                {/each}
              </Select>
        </fieldset>
        <fieldset class='fullwidth'>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Gramas de Caroidratos"
                invalid={error[1]}
                bind:value={carbo}
                color="secondary"
                on:change={() => validateField(1)}
            >
            </Textfield>
        </fieldset>
        <fieldset class='fullwidth'>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Descrição"
                bind:value={description}
                color="secondary"
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Select variant="filled" bind:value={measure} label="Medida de Referência" style='width: 100%'>
                <Option value={undefined}></Option>
                {#each MeasureMock as mm}
                  <Option value={mm.key}>{mm.description}</Option>
                {/each}
              </Select>
        </fieldset>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Quantidade da referência"
                bind:value={measureQuantity}
                color="secondary"
            >
            </Textfield>
        </fieldset>
    </form>
  </Content>
  <div class='actions'>
    <Button action="reject" on:click={closeHandler}>
      <Label>Cancelar</Label>
    </Button>
    <Button touch variant="unelevated" color="primary" on:click={handleSubmit}>
      <Label>Salvar</Label>
    </Button>
  </div>
</Dialog>

<style>
    .fullwidth{
        flex-grow: 2;
        width: 100%;
    }

    .actions{
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 8px;
        padding: 8px;
    }

    form{
        display: flex;
        flex-wrap: wrap;
    }
    fieldset {
        border: none;
        flex-grow: 1;
    }
</style>