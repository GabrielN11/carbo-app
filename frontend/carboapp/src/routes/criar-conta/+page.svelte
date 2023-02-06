<script lang="ts">
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import { isEmpty, isEqual } from "lodash-es";
    import signIn from "$lib/api/endpoints/auth/login";
    import UserLoginModel from "../../models/user/user-login-model";
    import { afterUpdate } from 'svelte';
    import { user } from "../../stores/user-store";
    import { goto } from '$app/navigation';
    import { displayToast } from "../../stores/toast-store";
    import createAccount from "$lib/api/endpoints/auth/create-account";
    import UserCreateModel from "../../models/user/user-create-model";


    let username: string = "";
    let password: string = "";
    let repeatPassword: string = "";
    let email: string = "";

    let error: boolean[] = [false, false, false, false];

    function validateField(index: number) {
        if(index === 0){
            if(isEmpty(username)){
                error[0] = true
            }else{
                error[0] = false
            }
        }else if(index === 1){
            if(isEmpty(password)){
                error[1] = true
            }else{
                error[1] = false
            }
        }else if(index === 2){
            if(isEmpty(repeatPassword)){
                error[2] = true
            }else{
                error[2] = false
            }
        }else{
            if(isEmpty(email)){
                error[3] = true
            }else{
                error[3] = false
            }
        }
    }

    async function handleSubmit(e: SubmitEvent){
        e.preventDefault();

        for(let i = 0; i<=3;i++){
            validateField(i)
        }

        if(!isEqual(password, repeatPassword)){
            error[1] = true
            error[2] = true
            return
        }

        if(error.includes(true))
            return

        try{
            const res = await createAccount(new UserCreateModel(username, password, email))

            displayToast(res.message, '#28a745', 5000)
            goto(`/criar-conta/${res.data.id}`)
        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
        }
    }


    afterUpdate(() => {
        if($user){
            goto('/')
        }
    })
</script>

<svelte:head>
    <title>Carbo App - Criar Conta</title>
    <meta
        name="description"
        content="Criar conta no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form on:submit={handleSubmit}>
        <h2>Criar uma conta</h2>
        <p>Crie uma conta para poder salvar os carboidratos de seus alimentos!</p>
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
                label="E-mail"
                type='email'
                invalid={error[3]}
                bind:value={email}
                color="secondary"
                on:change={() => validateField(3)}
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
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Confirme a senha"
                type='password'
                invalid={error[2]}
                bind:value={repeatPassword}
                color="secondary"
                on:change={() => validateField(2)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Button touch variant="outlined" color="secondary" type="submit" style='width: 100%'>
                <Label>Entrar</Label>
            </Button>
        </fieldset>
        <a href='/login'>Já tenho uma conta</a>
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

    @media(max-width: 600px), (max-height: 600px){
        form{
            padding-top: 0px;
        }
    }
</style>
