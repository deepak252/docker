package wrkload

type WrkResult struct {
	Url             string
	Method          string
	TimeTaken       string
	Connections     int
	TotalHits       int
	SuccessHits     int
	FailureHits     int
	SuccessMessages any
	FailureMessages any
}

type ApiData struct {
	Url    string
	Method string
	Body   any
}

type ApiDataBuilder struct {
	apiData ApiData
}

func (b *ApiDataBuilder) SetUrl(url string) *ApiDataBuilder {
	b.apiData.Url = url
	return b
}

func (b *ApiDataBuilder) SetMethod(method string) *ApiDataBuilder {
	b.apiData.Method = method
	return b
}

func (b *ApiDataBuilder) SetBody(body any) *ApiDataBuilder {
	b.apiData.Body = body
	return b
}

func (b *ApiDataBuilder) Build() *ApiData {
	return &b.apiData
}
