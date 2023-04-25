axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response.data)
})

//동기는 코드가 순서대로 실행되는 것이고, 다른 코드가 모두 수행할 때까지 그 이후의 코드가 실행되지 않음
//비동기는 병렬적으로 처리되어 빠름