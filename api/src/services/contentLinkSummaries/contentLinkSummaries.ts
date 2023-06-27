import type {
  QueryResolvers,
  MutationResolvers,
  ContentLinkSummaryRelationResolvers,
} from 'types/graphql'

import { db } from 'src/lib/db'

export const contentLinkSummaries: QueryResolvers['contentLinkSummaries'] =
  () => {
    return db.contentLinkSummary.findMany()
  }

export const contentLinkSummary: QueryResolvers['contentLinkSummary'] = ({
  id,
}) => {
  return db.contentLinkSummary.findUnique({
    where: { id },
  })
}

export const createContentLinkSummary: MutationResolvers['createContentLinkSummary'] =
  ({ input }) => {
    return db.contentLinkSummary.create({
      data: input,
    })
  }

export const updateContentLinkSummary: MutationResolvers['updateContentLinkSummary'] =
  ({ id, input }) => {
    return db.contentLinkSummary.update({
      data: input,
      where: { id },
    })
  }

export const deleteContentLinkSummary: MutationResolvers['deleteContentLinkSummary'] =
  ({ id }) => {
    return db.contentLinkSummary.delete({
      where: { id },
    })
  }

export const ContentLinkSummary: ContentLinkSummaryRelationResolvers = {
  Content: (_obj, { root }) => {
    return db.contentLinkSummary
      .findUnique({ where: { id: root?.id } })
      .Content()
  },
  LinkSummary: (_obj, { root }) => {
    return db.contentLinkSummary
      .findUnique({ where: { id: root?.id } })
      .LinkSummary()
  },
}