var app = new Vue({
    el: '#app',
    data: {
        results: []
    },
    mounted() {
        axios.get("http://127.0.0.1:8000/api/automobiles")
            .then(response => {
                this.results = response.data.fields
            })
    }
})
