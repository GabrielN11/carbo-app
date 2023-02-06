<script lang='ts'>
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import validateAccount from "$lib/api/endpoints/auth/validate-account";
    import Button, { Label } from "@smui/button";
    import Textfield from "@smui/textfield";
    import { isEmpty, toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import UserValidationModel from "../../../models/user/user-validation-model";
    import { displayToast } from "../../../stores/toast-store";
    import { user } from "../../../stores/user-store";

    let id: number;

    let code: string = '';
    let error: boolean = false;

    async function handleSubmit(e: SubmitEvent){
        e.preventDefault()

        if(isEmpty(code)){
            error = true
            return
        }

        try{
            const res = await validateAccount(new UserValidationModel(id, code))

            localStorage.setItem('usertoken', res.data.token)

            user.update(() => res.data)

            displayToast(res.message, '#28a745', 5000)
            goto('/')

        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
        }
    }

    onMount(() => {
        try{
            id = toNumber($page.url.pathname.split('/')[2])

            if(isNaN(id)) throw new Error()
        }catch(e: any){
            goto('/')
        }
    })
</script>

<svelte:head>
    <title>Carbo App - Validação</title>
    <meta
        name="description"
        content="Validar conta no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form on:submit={handleSubmit}>
        <h2>Recuperação de conta</h2>
            <fieldset>
                <p>
                    Enviamos um código para o endereço de e-mail, digite
                    o código que você recebeu no e-mail abaixo.
                </p>
            </fieldset>
            <fieldset>
                <Textfield
                    style="width: 100%"
                    variant="filled"
                    label="Código"
                    invalid={error}
                    bind:value={code}
                    color="secondary"
                />
            </fieldset>
            <fieldset>
                <Button
                    variant="outlined"
                    color="secondary"
                    type="submit"
                    style="width: 100%"
                >
                    <Label>Validar Conta</Label>
                </Button>
            </fieldset>
    </form>
</section>

<style>
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        padding-top: 75px;
    }

    fieldset {
        width: 254px;
        border: none;
    }

    @media (min-width: 600px) {
        fieldset {
            width: 400px;
        }
    }

    @media(max-width: 600px), (max-height: 600px){
        form{
            padding-top: 0px;
        }
    }
</style>
