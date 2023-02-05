<script lang="ts">
    import welcome from "$lib/images/svelte-welcome.webp";
    import welcome_fallback from "$lib/images/svelte-welcome.png";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";

    import Toast from "../../components/toast/toast.svelte";
    import { afterUpdate } from "svelte";
    import { goto } from "$app/navigation";
    import { user } from "../../stores/user-store";
    import recoverEmail from "$lib/api/endpoints/auth/recover-email";
    import UserEmailModel from "../../models/user/user-email-model";
    import { displayToast } from "../../stores/toast-store";
    import validateCode from "$lib/api/endpoints/auth/validate-code";
    import changePassword from "$lib/api/endpoints/auth/change-password";
    import { isEmpty, isEqual } from "lodash-es";
    import UserPasswordModel from "../../models/user/user-password-model";

    let email: string = "";
    let code: string = "";
    let password: string = "";
    let repeatPassword: string = "";

    let userId: number;

    let error: boolean = false;
    let equalPass: boolean = false;

    let step: number = 1;

    async function submitEmail() {
        try {
            if(isEmpty(email)){
                error = true
                return
            }
            const res = await recoverEmail(new UserEmailModel(email));

            userId = res.data.id;
            step = 2;

            displayToast(res.message, "#28a745", 5000);
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
        }finally{
            error = false
        }
    }

    async function submitCode() {
        try {
            if (isEmpty(code)) {
                error = true;
                return;
            }
            const res = await validateCode(userId, code);

            step = 3;

            displayToast(res.message, "#28a745", 7000);
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
        } finally {
            error = false;
        }
    }

    async function submitPassword() {
        try {
            if (!isEqual(password, repeatPassword)) {
                equalPass = true;
                throw new Error("Senhas não conferem.");
            }
            const res = await changePassword(
                new UserPasswordModel(password),
                userId
            );

            displayToast(res.message, "#28a745", 5000);
            goto("/login");
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
        }
    }

    function onSubmit(e: SubmitEvent) {
        if (step === 1) {
            submitEmail();
            return;
        }

        if (step === 2) {
            submitCode();
            return;
        }

        submitPassword();
    }

    afterUpdate(() => {
        if ($user) {
            goto("/");
        }
    });
</script>

<svelte:head>
    <title>Carbo App - Recuperar Conta</title>
    <meta
        name="description"
        content="Recuperação de senha no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form on:submit={onSubmit}>
        <h2>Recuperação de conta</h2>
        {#if step === 1}
            <p>Digite o e-mail registrado na sua conta.</p>
            <fieldset>
                <Textfield
                    style="width: 100%"
                    variant="filled"
                    type="email"
                    label="E-mail"
                    invalid={error}
                    bind:value={email}
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
                    <Label>Prosseguir</Label>
                </Button>
            </fieldset>
        {:else if step === 2}
            <fieldset>
                <p>
                    Enviamos um código para o endereço de e-mail {email}, digite
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
                    <Label>Validar</Label>
                </Button>
            </fieldset>
        {:else if step === 3}
            <p>Escolha uma nova senha...</p>
            <fieldset>
                <Textfield
                    style="width: 100%"
                    variant="filled"
                    label="Senha"
                    invalid={error || equalPass}
                    bind:value={password}
                    color="secondary"
                    type='password'
                />
            </fieldset>
            <fieldset>
                <Textfield
                    style="width: 100%"
                    variant="filled"
                    label="Confirme a Senha"
                    invalid={error || equalPass}
                    bind:value={repeatPassword}
                    color="secondary"
                    type='password'
                />
            </fieldset>
            <fieldset>
                <Button
                    variant="outlined"
                    color="secondary"
                    type="submit"
                    style="width: 100%"
                >
                    <Label>Alterar</Label>
                </Button>
            </fieldset>
        {/if}
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
</style>
