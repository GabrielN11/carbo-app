<script lang="ts">
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import { isEmpty } from "lodash-es";
    import signIn from "$lib/api/endpoints/auth/login";
    import UserLoginModel from "../../models/user/user-login-model";
    import { afterUpdate } from 'svelte';
    import { user } from "../../stores/user-store";
    import { goto } from '$app/navigation';
    import { displayToast } from "../../stores/toast-store";


    let username: string = "";
    let password: string = "";

    let error: boolean[] = [false, false];

    function validateField(index: number) {
        if(index === 0){
            if(isEmpty(username)){
                error[0] = true
            }else{
                error[0] = false
            }
        }else{
            if(isEmpty(password)){
                error[1] = true
            }else{
                error[1] = false
            }
        }
    }

    async function onSubmit(e: SubmitEvent) {
        e.preventDefault();

        validateField(0);

        validateField(1);

        if (error.includes(true)) return;

        try{
            const res = await signIn(new UserLoginModel(username, password))

            localStorage.setItem('usertoken', res.data.token)

            user.update(() => res.data)

            displayToast(`Bem-vindo ${res.data.username}!`, '#28a745', 4000)

            goto('/', {replaceState: true})

        }catch(e: any){
            displayToast(e.message, '#dc3545', 2500)
        }
    }

    afterUpdate(() => {
        if($user){
            goto('/')
        }
    })
</script>

<svelte:head>
    <title>Carbo App - Entrar</title>
    <meta
        name="description"
        content="Login no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form on:submit={onSubmit}>
        <h2>Login</h2>
        <p>Entre para poder salvar os carboidratos de seus alimentos!</p>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Usuário"
                invalid={error[0]}
                bind:value={username}
                color="secondary"
                on:change={() => validateField(0)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Senha"
                type='password'
                invalid={error[1]}
                bind:value={password}
                color="secondary"
                on:change={() => validateField(1)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Button touch variant="outlined" color="secondary" type="submit" style='width: 100%'>
                <Label>Entrar</Label>
            </Button>
        </fieldset>
        <a href='/recuperar'>Esqueci minha senha</a>
    </form>
</section>

<style>
    p {
        padding: 0 5px;
        text-align: center;
    }
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

    @media(min-width: 600px){
        fieldset{
            width: 400px;
        }
    }
</style>
