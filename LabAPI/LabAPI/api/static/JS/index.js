var app = new Vue({
    el:'#index',
    data:{
        labstudent:[]
    },
    mounted(){
        this.getData()
    },
    methods:{
        getData:function(){
            var self = this
            reqwest({
                url:'/api/stuuser/',
                method:'get',
                type:'json',
                success:function(data){
                    self.labstudent = data.labstudent
                }
            })
        }
    }
})