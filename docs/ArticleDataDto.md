# ArticleDataDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier. | 
**name** | **str** | The name (or brand name) for this article, usually given by the supplier or vendor. | [optional] 
**article_number** | **str** | An article number that describes it, useful when integrating other systems. | [optional] 
**quantity** | **float** | Quantity for this article. If this is used within a Position, the quantity here should be the quantity required for the full quantity of the position, not for a single unit. | 
**unit_tag** | **str** | The unit tag for this single ArticleData. | [optional] 
**description** | **str** | This is an optional text element that can be used to further describe the ArticleData. | [optional] 
**short_text** | **str** | Short description for this ITextElement element. | [optional] 
**long_text** | **str** | Detailed description for this ITextElement element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText. | [optional] 
**html_long_text** | **str** | This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


