Vue.component("vue", {
    data: function() {
        return {
            message: "Hello, Vue!"
        }
    },
    template: `
        <h1>{{ message }}</h1>
    `
});

new Vue({ el: "#js-message" })
